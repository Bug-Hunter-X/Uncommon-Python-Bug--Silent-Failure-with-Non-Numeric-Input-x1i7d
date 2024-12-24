# Uncommon Python Bug: Silent Failure with Non-Numeric Input

This repository demonstrates a subtle bug in a Python function designed to calculate the average of a list of numbers. The bug arises when the input list contains non-numeric elements. The function doesn't explicitly check for this condition, resulting in a `TypeError` exception being raised silently if such data is provided.