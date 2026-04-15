# PROBLEM DESCRIPTION AND SOLUTION DESIGN:
# In an audio work station, users want to be able to apply multiple effects
# to their audio file. Composing and currying is useful in this scenario
# because instead of writing one large functions, a more flexible system
# where effects can be reused, reordered, stacked, and customized easily 
# is more powerful. Currying will allow us to create effects and
# composition will let us chain the effects into a pipeline.

from functools import partial, reduce


# Audio Effects
# Adjust volume by a percentage
def adjust_volume(percent):
    return lambda signal: [x * percent for x in signal]

# def add_echo(delay, decay):
#     def effect(signal):
#         output = signal[:]
#         for i in range(delay, len(signal)):
#             output[i] += signal[i - delay] * decay
#         return output
#     return effect

# Adds a copy of the rest of the array after the delay and reduces volume by half
def add_echo(delay):
    def effect(signal):
        newSignal = signal[:]
        for i in range(delay, len(signal)):
            newSignal.append(signal[i]*.5)
        return newSignal
    return effect

# Creates a threshold (maximum and minimum) and sets any value above or below to that value
def distort(threshold):
    return lambda signal: [
        max(min(x, threshold), -threshold) for x in signal
    ]


# Compose Function
def compose(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions)


# Simulated Audio Signal
audio_signal = [0.2, 0.5, -0.4, 0.7, -0.8, 0.3]


# Create Curried Effects
volume = adjust_volume(0.8)
echo = add_echo(3)
clipping = distort(0.6)


# Compose Effects Pipeline
audio_pipeline = compose(clipping, echo, volume)

# Apply pipeline
processed_audio = audio_pipeline(audio_signal)

print("Original:", audio_signal)
print("Processed:", processed_audio)

# SOLUTION:
# Currying was used to create reusable functions like add_echo, distort,
# and adjust_volume. Composition is used to chain these effects into
# one pipeline. This allows a modular design in which effects can be
# easily reordered. The benefits of this approach is its flexibility
# and modularity in which effects can be reused and reordered.
# Another benefit is the scalability of a program like this. More functions
# can be added later on in the future and would still work.

# REFLECTION:
# A challenge I had is debugging. Debugging and overall looking through the
# code can sometimes be hard to follow when there are many functions
# within each other. However, composing the pipeline in the end becomes
# extremely readable and once these functions are built in, they don't
# really need to be changed.
#
# OpenAI. (2026). ChatGPT (April 2026 version) [Large language model]. https://chat.openai.com/chat.
# ChatGPT was used to help debug certain components of the code.