# hash-cracker

A command-line Python tool for cracking hashes (MD5, SHA-1, SHA-256, etc.) using a dictionary attack against a wordlist.

## ⚠️ Disclaimer

This project was built exclusively for educational purposes and cybersecurity learning.
It should only be used against hashes you own, in lab environments, or in authorized CTFs.
Do not use this tool against systems or data you don't have explicit permission to test — doing so may be illegal.

## Features

- Support for multiple hashing algorithms (MD5, SHA-1, SHA-256, and any others supported by `hashlib`)
- Reads wordlists from `.txt` files
- Measures execution time
- Handles errors (missing file, invalid algorithm)

## What I learned

Building this project helped me understand how password hashing works, 
the difference between dictionary attacks and brute-force approaches, 
and why algorithms like MD5 and SHA-1 are considered insecure for 
storing passwords compared to bcrypt or Argon2.

## Requirements

- Python 3.8 or higher
- No external dependencies (uses only the Python standard library)

## Installation

```bash
git clone https://github.com/Omelhor123/hash-cracker.git
cd hash-cracker
```

## Usage

```bash
python hash_cracker.py <target_hash> -w wordlist.txt -a md5
```

| Argument | Description | Required |
|---|---|---|
| `hash` | The target hash you want to crack | Yes |
| `-w`, `--wordlist` | Wordlist file to use (default: `rockyou.00.txt`) | No |
| `-a`, `--algorithm` | Hashing algorithm to use (default: `md5`) | No |

### Example

```bash
$ python hash_cracker.py 5f4dcc3b5aa765d61d8327deb882cf99 -w wordlist.txt -a md5

Match found: password

**********************
Finished
Execution time: 0.03 seconds
**********************
```

## Wordlist

This project was tested using the **rockyou.00.txt** wordlist, a well-known list widely used in offensive security.
You can download it [here](https://github.com/danielmiessler/SecLists) (not included in this repository due to its size).

## Future improvements

- [ ] Add brute-force attack support
- [ ] Add multithreading to speed up processing on large wordlists
- [ ] Auto-detect the hashing algorithm based on hash length

## License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
