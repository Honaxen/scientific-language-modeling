"""
ner.py
------
Scientific Named Entity Recognition using rule-based pattern matching.
Detects models, metrics, datasets, and methods in scientific text.
"""

import re
from collections import Counter


ENTITY_PATTERNS = {
    "MODEL": [
        r'\bTransformer\b', r'\bBERT\b', r'\bGPT\b', r'\bLSTM\b',
        r'\bRNN\b', r'\bCNN\b', r'\bEncoder[-\s]Decoder\b',
        r'\bMulti[-\s]Head Attention\b', r'\bSelf[-\s]Attention\b',
    ],
    "METRIC": [
        r'\bBLEU\b', r'\bperplexity\b', r'\baccuracy\b',
        r'\bF1\b', r'\bROUGE\b', r'\bPrecision\b', r'\bRecall\b',
    ],
    "DATASET": [
        r'\bWMT\b', r'\bImageNet\b', r'\bSQuAD\b', r'\bGLUE\b',
        r'\bEnglish[-\s]German\b', r'\bEnglish[-\s]French\b',
    ],
    "METHOD": [
        r'\battention mechanism\b', r'\bdropout\b', r'\blayer normalization\b',
        r'\bgradient descent\b', r'\bbeam search\b', r'\bpositional encoding\b',
    ]
}

CLAIM_PATTERNS = [
    r'we propose', r'we present', r'we introduce', r'we show',
    r'we demonstrate', r'we achieve', r'our model', r'our approach',
    r'outperform', r'state.of.the.art', r'novel', r'first to',
]


def extract_entities(text: str, patterns: dict = ENTITY_PATTERNS) -> dict:
    """Extract scientific entities using regex patterns."""
    results = {}
    for entity_type, pattern_list in patterns.items():
        found = []
        for pattern in pattern_list:
            matches = re.findall(pattern, text, re.IGNORECASE)
            found.extend(matches)
        results[entity_type] = Counter(found)
    return results


def extract_claims(text: str, patterns: list = CLAIM_PATTERNS) -> list:
    """Extract sentences containing claim signal words."""
    sentences = re.split(r'(?<=[.!?])\s+', text)
    claims = []
    for sentence in sentences:
        sentence = sentence.strip()
        if len(sentence) < 20:
            continue
        for pattern in patterns:
            if re.search(pattern, sentence, re.IGNORECASE):
                claims.append({
                    'sentence': sentence,
                    'signal': pattern,
                    'length': len(sentence.split())
                })
                break
    return claims