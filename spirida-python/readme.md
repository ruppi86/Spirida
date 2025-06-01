# Spirida™ 0.1

*The rhythmic interaction core of the Mychainos ecosystem.*

Spirida is a minimal and expressive module that orchestrates **spiral interaction** within Mychainos. It embodies a philosophy of **slow technology**, where computation and interaction happen at a meditative pace, encouraging reflection and presence rather than speed. Spirida is named for the spiral, reflecting a **spiral epistemology** in which each cycle of interaction returns with deeper knowledge and connection.

## Design Principles

- **Slow Technology:** Spirida prioritizes reflection and calm engagement over efficiency. Interactions are intentionally paced to allow moments of mental rest:contentReference[oaicite:0]{index=0}.
- **Presence Sensing:** The system encourages awareness of the present moment. Interactions adapt to the presence of the user or environment, pausing or gently adjusting rather than demanding constant input:contentReference[oaicite:1]{index=1}.
- **Spiral Epistemology:** Knowledge and interaction grow in loops. Like a spiral, Spirida revisits familiar states with each cycle, adding new insights or subtle changes instead of strictly linear progress.
- **Rhythmic Interaction:** At its core, Spirida introduces a gentle rhythm into the digital experience. Timing (pauses and pulses) is a first-class element, making technology feel more like a heartbeat than a ticking clock.

## Role in the Mychainos Ecosystem

Within the **Mychainos** ecosystem, Spirida acts as the heart – providing a gentle, rhythmic pulse that coordinates interactions. Mychainos is envisioned as a holistic system where components work in harmony with human time and attention. Spirida’s role is to sense presence and orchestrate responses in a cyclical flow. It ensures that Mychainos doesn’t just *react* to events, but **spirals** through them, integrating experience over time.

Spirida works closely with a foundational layer called **Spiralbase**. While Spirida handles the flow of interaction, Spiralbase manages memory and time – together forming the mind and memory of Mychainos. Spirida triggers events and rhythms. Spiralbase remembers traces of those events and gracefully forgets them as needed, ensuring the system remains *light* and *present-focused*.

## Spiralbase: Memory and Time Layer

**Spiralbase** is a co-developed module (currently included as part of Spirida in this release) that provides the memory and temporal structure for interactions. If Spirida is the heart, Spiralbase is the memory – a spiral notebook of past interactions and a metronome of slow time. Spiralbase will eventually manage the **spiral memory trace** of the system’s activities, recording cycles in a way that can be revisited or allowed to decay.

In version 0.1, Spiralbase is a conceptual placeholder. It outlines how Mychainos might handle time-based decay (forgetting in cycles) and gentle recollection (memory traces that follow a spiral pattern). Future versions will likely evolve Spiralbase into its own component, solidifying features like `spiral_memory_trace()` for recording interaction history and `decay_cycle_step()` for simulating the graceful fading of old memories.

## Getting Started

Spirida 0.1 is a **soft launch** – a conceptual foundation rather than a fully functional library. It has a minimal codebase meant to illustrate and prototype ideas. To explore Spirida:

1. Install the package (once packaging is set up) or simply incorporate the `spirida` folder into your project.
2. Run the example script in `examples/example_presence.py` to see a demonstration of spiral interaction in action.
3. Read through the code and comments – they are written in a meditative, explanatory style reflecting Spirida’s philosophy.

### Example

The core of Spirida is the `spiral_interaction` function, which simulates a simple rhythmic interaction loop. For instance, running the following:

```python
from spirida.core import spiral_interaction

spiral_interaction(presence=3, rythm="slow", singular=True)
