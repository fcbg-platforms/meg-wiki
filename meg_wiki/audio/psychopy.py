from __future__ import annotations  # c.f. PEP 563 and PEP 649

from typing import TYPE_CHECKING

import psychtoolbox as ptb
from bsl.triggers import MockTrigger, ParallelPortTrigger
from psychopy.clock import wait
from psychopy.sound.backend_ptb import SoundPTB as Sound

from ..utils._checks import check_type, ensure_int
from ..utils._docs import fill_doc
from ..utils.logs import logger

if TYPE_CHECKING:
    from typing import Tuple


@fill_doc
def psychopy_uncompensated(
    address: str, frequency: float, volume: float = 0.2, n_repetition: int = 100
) -> None:
    """Run a loop of pure tone auditory stimuli using PsychoPy.

    Before each stimuli, a trigger is delivered on the first pin of the DB-25
    parallel port. The trigger is not compensated for the stimuli delay.

    Parameters
    ----------
    %(address)s
    %(frequency)s
    volume : float
        Volume at which the sound is played, between 0 and 1.
    %(n_repetition)s

    Notes
    -----
    The sound duration is set to 200 ms. The hanning window to smooth the onset and
    offset is disabled.
    """
    _, _, n_repetition = _check_args(frequency, volume, n_repetition)
    # error checking on the parallel-port argument is handled by BSL directly
    trigger = MockTrigger() if address == "mock" else ParallelPortTrigger(address)
    sound = Sound(value=frequency, volume=volume, secs=0.2, hamming=False)
    wait(0.1)
    for k in range(1, n_repetition + 1, 1):
        logger.info("Event %i / %i", k, n_repetition)
        trigger.signal(1)
        sound.play()
        wait(0.2, hogCPUperiod=0.1)
        sound.stop()
        wait(0.8, hogCPUperiod=0.3)
    del sound
    del trigger


@fill_doc
def psychopy_compensated(
    address: str, frequency: float, volume: float = 0.2, n_repetition: int = 100
) -> None:
    """Run a loop of pure tone auditory stimuli using PsychoPy.

    Before each stimuli, a trigger is delivered on the first pin of the DB-25
    parallel port. The trigger is compensated for the stimuli delay.

    Parameters
    ----------
    %(address)s
    %(frequency)s
    volume : float
        Volume at which the sound is played, between 0 and 1.
    %(n_repetition)s

    Notes
    -----
    The sound duration is set to 200 ms. The hanning window to smooth the onset and
    offset is disabled.
    """
    _, _, n_repetition = _check_args(frequency, volume, n_repetition)
    trigger = MockTrigger() if address == "mock" else ParallelPortTrigger(address)
    sound = Sound(value=frequency, volume=volume, secs=0.2, hamming=False)
    wait(0.1)
    for k in range(1, n_repetition + 1, 1):
        logger.info("Event %i / %i", k, n_repetition)
        now = ptb.GetSecs()
        sound.play(when=now + 0.5)
        wait(0.5, hogCPUperiod=0.2)
        trigger.signal(1)
        wait(0.2, hogCPUperiod=0.1)
        sound.stop()
        wait(0.3, hogCPUperiod=0.1)
    del sound
    del trigger


def _check_args(
    frequency: float, volume: float = 0.2, n_repetition: int = 100
) -> Tuple[float, float, int]:
    """Check arguments used in PsychoPy's functions."""
    check_type(frequency, ("numeric",), "frequency")
    if frequency <= 0:
        raise ValueError("The sound frequency (Hz) must be a strictly positive number.")
    check_type(volume, ("numeric",), "volume")
    if volume < 0 or 1 < volume:
        raise ValueError("The volume must be defined between 0 and 1.")
    n_repetition = ensure_int(n_repetition, "n_repetition")
    return frequency, volume, n_repetition