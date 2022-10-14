# Fio libaio ioengine vs xNVMe libaio backend polling comparison

| | xNVMe libaio backend | fio libaio ioengine | | xNVMe libaio backend (hipri) | fio libaio ioengine (userspace_reap) |
| :-- | --: | --: | --: | --: | --: |
| Mean total latency (ns) | 8970 | 8758	| | 5727 | 5527 |
| IOPS | 107k | 109k | | 170k | 176k |
| CPU usr | 12.19% | 13.73% | | 34.86% | 87.57% |
| CPU sys | 35.20% | 29.65% | | 65.13% | 12.43% |
| Context switches | 6421050 | 6562188 | | 263 | 272 |

* Fio job: [link](xnvme-compare.fio)
* Fio output: [link](xnvme-compare.output)
