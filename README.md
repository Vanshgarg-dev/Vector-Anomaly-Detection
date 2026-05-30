# Vector-Based Anomaly Detection with Qdrant

A novel approach to anomaly detection using **vector embeddings** and **Qdrant's recommendation engine**. Instead of traditional statistical methods, this technique leverages semantic similarity in vector space to surface outliers — no labeled training data required.

## How It Works

1. **Embed your data** into vector space using a sentence transformer.
2. **Provide a few known-good examples** and treat them as *negative* inputs to Qdrant's recommendation API — this returns the points *most dissimilar* to the good examples (i.e., likely anomalies).
3. **Use those discovered anomalies as *positive* inputs** to find even more anomalous points in the dataset.

This two-step strategy requires only 2–3 examples of normal data to bootstrap anomaly discovery across an entire dataset.

```
Known-good examples (negative) → Discover initial anomalies
                                        ↓
              Initial anomalies (positive) → Discover all anomalies
```

## Demo

### Toy Example: Cities vs. Fruits

A dataset of 120+ city names is mixed with 10 fruit names. Using just 4 city names as known-good examples, the system correctly identifies all 10 fruits as anomalies:

```
Step 1 — Using cities as negative examples:
  Anomaly: Watermelon  (Score: -0.567)
  Anomaly: Papaya      (Score: -0.570)
  Anomaly: Blueberry   (Score: -0.573)

Step 2 — Using found anomalies as positive examples:
  Anomaly: Watermelon   (Score: 0.750)
  Anomaly: Blueberry    (Score: 0.750)
  Anomaly: Strawberry   (Score: 0.692)
  Anomaly: Mango        (Score: 0.688)
  ... all 10 fruits detected
```

### Real-World Example: Credit Card Transactions

Applied to a credit card transaction dataset with injected anomalous entries (unusual Customer IDs, extreme amounts, unexpected categories). The system successfully surfaces the synthetic fraud cases.

## Tech Stack

| Component | Technology |
|---|---|
| Vector DB | [Qdrant](https://qdrant.tech/) (in-memory) |
| Embeddings | [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) via SentenceTransformers |
| Data | pandas, NumPy |

## Quick Start

```bash
pip install qdrant-client sentence-transformers pandas
jupyter notebook Anomaly_Detection.ipynb
```

## Project Structure

```
qdrant-new/
├── Anomaly_Detection.ipynb    # Main notebook — toy + real-world examples
├── datalter.py                # Utility to inject anomalies into CSV data
├── updated_file.csv           # Sample transaction dataset with anomalies (16 KB)
└── README.md
```

## Key Insight

Traditional anomaly detection often requires labeled datasets or statistical assumptions about data distributions. This approach needs **neither** — just a vector database and a few examples of what "normal" looks like. Useful for:

- **Cold-start scenarios** where labeled anomaly data doesn't exist
- **Mixed-type datasets** where statistical methods struggle
- **Exploratory analysis** to quickly surface unexpected patterns

### In collaboration with [Superteams.ai](https://www.superteams.ai/)

