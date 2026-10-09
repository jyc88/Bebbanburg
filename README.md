# Performance Improvement Ideas

This repository captures an example of the highest-impact, lowest-effort performance improvement: memoizing repeated expensive computations. The list below outlines ten practical optimizations that typically yield strong gains with modest code changes.

## 1) Memoize repeated expensive calculations
Use a cache for deterministic work that is computed repeatedly with the same inputs.

## 2) Eliminate N+1 database queries
Fetch related rows in bulk instead of issuing a query per object.

## 3) Add database indexes and projection
Index frequently filtered columns and select only the fields required by the caller.

## 4) Batch writes and network calls
Combine independent requests or writes to lower per-operation overhead.

## 5) Reduce object churn and allocations
Reuse buffers, avoid unnecessary DTO creation, and prefer primitives where possible.

## 6) Cache static or slowly changing content
Keep frequently accessed configuration, pricing, or reference data in memory.

## 7) Use pagination and lazy loading
Load only what the user needs instead of materializing giant result sets in memory.

## 8) Stream large payloads
Avoid buffering entire files or responses in memory when chunked processing is enough.

## 9) Parallelize CPU-bound work safely
Spread independent compute tasks across worker pools, but avoid over-parallelizing I/O-heavy code.

## 10) Avoid repeated serialization and formatting work
Cache rendered output or precompute stable strings when the inputs are unchanged.

## Implemented example
The repository includes a lightweight memoization utility in `performance_optimization.py`. It demonstrates the classic tradeoff: a small amount of memory for a large reduction in repeated CPU work.
