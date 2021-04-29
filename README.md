# dxtractor
### extract subdomains based on level.

## example :
### 1. extract third level domains :
`cat subdomains.txt | python3 dxtractor.py`
### Or
`python3 dxtractor.py -file subdomains.txt`

### 2. extract forth level domains using `-count` flag:
`cat subdomains.txt | python3 dxtractor.py -count 4`
### Or
`python3 dxtractor.py -file subdomains.txt -count 4`
