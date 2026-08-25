# Experiments - plan

## Research questions
### RQ1 - CNN depth
How does CNN depth affect image-captioning performance?
1. Shallow CNN -> RNN
2. Medium CNN -> RNN
3. Deep CNN -> RNN

### RQ2 - Visual representation
How does the representation passed from the CNN to the text decoder affect caption generation?
1. CNN -> feature vector -> RNN
2. CNN -> spatial feature map -> RNN

### RQ3 - Decoder Architecture
How does decoder architecture affect generated captions?
1. CNN -> visual representation -> RNN
2. CNN -> visual representation -> Transformer