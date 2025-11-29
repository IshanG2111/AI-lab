```markdown
# AI-lab

All AI lab materials will be shared here. This repository is intended as a central place for lecture notes, example code, datasets (or links to them), assignment briefs, slides, and helpful resources for learning and experimenting with Artificial Intelligence.

---

## Quick overview

- Audience: Beginners to intermediate students exploring AI, machine learning, and deep learning.
- Goal: Provide concise explanations, runnable code snippets, visual aids (including GIFs), and references so you can learn by doing.

---

## What is AI?

Artificial Intelligence (AI) is a field of computer science focused on creating systems that can perform tasks that normally require human intelligence. This includes:

- Perception (e.g., recognizing images or speech)
- Reasoning and planning
- Learning from data (machine learning)
- Natural language understanding and generation
- Robotics and control

Two major approaches:

- Symbolic AI: Hand-coded rules and logic.
- Statistical / Learning-based AI: Algorithms that learn patterns from data (the dominant approach today).

---

## Why Python for AI?

Python is the de-facto language for AI and machine learning for several reasons:

- Easy to read and write (great for rapid prototyping).
- Huge ecosystem: NumPy, pandas, scikit-learn, TensorFlow, PyTorch, Keras, Hugging Face, and more.
- Strong community and many tutorials, examples, and pre-trained models.
- Excellent tooling for data manipulation, visualization, and deployment.

---

## Quick code snippets

Here are a few small, runnable examples to get you started. Copy and paste them into a .py file or a Jupyter notebook.

1) Basic Python + NumPy

```python
import numpy as np
# Create a 2x2 matrix and compute its transpose and mean
A = np.array([[1, 2], [3, 4]])
print("A:\n", A)
print("Transpose:\n", A.T)
print("Mean:", A.mean())
```

2) Simple scikit-learn example (train a tiny logistic regression)

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)
print("Test accuracy:", accuracy_score(y_test, model.predict(X_test)))
```

---

![Training gif](https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif)


## Contributing

If you want to add materials: fork the repo, create a branch, add your content (notebooks should be cleared of heavy outputs where possible), and open a pull request. Use clear commit messages and add a short description in your PR explaining the content.
