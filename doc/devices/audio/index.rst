.. include:: ../../links.inc

Audio stimulation
=================

2 separate audio stimulation systems are available. Each system has a different
frequency and latency response.

.. grid::

  .. grid-item-card:: Natus TIP-300
    :link: natus.html
    :link-type: url
    :text-align: center

    .. image:: ../../_static/devices/natus-tip-300.png

  .. grid-item-card:: SoundPixx
    :link: soundpixx.html
    :link-type: url
    :text-align: center

    .. image:: ../../_static/devices/soundpixx-light.png
        :class: only-light

    .. image:: ../../_static/devices/soundpixx-dark.png
        :class: only-dark

Both audio stimulation systems are connected to a USB audio interface `Crimson 3`_ from
`SPL`_.

.. figure:: ../../_static/devices/crimson.png
    :width: 700
    :align: center

    The configuration is detailed on labels on the `Crimson 3`_.

Select Natus TIP-300 or SoundPixx
---------------------------------

The button ``Speakers: A to B`` selects the system in use. If the button is ``OFF``, the
speakers ``A`` corresponding to the :ref:`devices/audio/natus:Natus TIP-300` system
is selected. If the button is ``ON``, the speakers ``B`` corresponding to the
:ref:`devices/audio/soundpixx:SoundPixx` system is selected.

.. tip::

    If the :ref:`devices/audio/soundpixx:SoundPixx` is in-use, don't forget to
    turn on the SoundPixx controller.

Microphone inputs 1/2
---------------------

The 2 microphone inputs 1 and 2 must be used without 48V phantom power and without
high-pass filter. The microphone 2 is connected to the black microphone used to speak to
the participant through the in-ear headphones. To enable the black microphone, both the
``Inputs: 1|2`` and ``Inputs: Mono`` button must be enabled.

.. tip::

    The black microphone has a low volume. Don't forget to turn the knob of input 2 to
    a high value. However, don't set it to max as it would leave a background noise. The
    LEDs ``SIG`` of the microphone input 2 should remain off while the black microphone
    is not in use.

Audio sources
-------------

Auditory stimulation can come from 2 sources: the `Chronos`_ if `E-Prime`_ is used or
directly the computer sound (DAW). Only one of the 2 sources should be active at a time.
To use the sound from the `Chronos`_, the button ``Sources: RCA`` must be enabled. To
use the sound from the computer, the button ``DAW: 1|2`` must be enabled.

.. note::

    On Windows, the computer sends sound to a single channel, ``DAW: 1|2``. However on
    Linux, it sends sound to both channels, ``DAW: 1|2`` and ``DAW: 3|4``, thus enabling
    both yields a higher volume.

Monitoring feedback
-------------------

The sound from the audio stimulation system is redirected on an MEG analogical channel,
``MISC 006``, from the ``Phones 1`` output.

2 Bose speakers are used to monitor the sound played through the audio stimulation
system. The Bose speakers are connected on ``Phones 2`` and volume is adjusted both with
a knob on the speakers and with the knob ``Phones 2`` on the `Crimson 3`_.

Main volume
-----------

The main volume knob affects the volume from all sources. The volume should be gradually
increased from a low value up-to the desired value to prevent loud sound from deafening
participants.
