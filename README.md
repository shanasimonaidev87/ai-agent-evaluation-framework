# AI Agent Evaluation Framework

## Project Overview
A Python research engineering project for evaluating
AI model responses and agent trajectories.

## Components
- LLM-as-a-Judge evaluation
- Alignment benchmark evaluation
- Agent trajectory analysis
- Rule-based failure detectors
- Semantic failure detection using an LLM
- Precision, recall, F1, and accuracy evaluation
- False-positive analysis

## Experimental Results

Milestone 17:
8/8 correct baseline classifications.

Milestone 18:
6/6 correct synthetic alignment classifications.

Milestone 19:
8/8 correct advanced synthetic classifications.

Milestone 22:
Version 1 baseline (8 synthetic cases):
Accuracy: 87.5%
Precision: 100%
Recall: 66.7%
F1: 80%

Milestone 24:
Version 2 holdout (8 synthetic cases):
Accuracy: 50%
Precision: 33.3%
Recall: 25%
F1: 25%

Milestone 26:
Semantic judge Version 3 (10 cases):
Accuracy: 80%
Precision: 60%
Recall: 100%
F1: 75%

Milestone 28:
Semantic judge Version 4 (10 diagnostic cases):
Accuracy: 100%
Precision: 100%
Recall: 100%
F1: 100%

## Research Limitations
The datasets are small and synthetic.
Version 4 was tuned using known diagnostic failures.
Independent evaluation on new cases is necessary
before making generalization claims.

## Future Work
- Larger independently labeled datasets
- Real agent execution logs
- Error attribution
- Prompt injection evaluation
- Human/AI judge agreement
- Reproducible benchmark reporting
