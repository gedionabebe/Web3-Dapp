# Web3-Dapp
## Certificate generation, Distribution, and Value transfer with Algorand NFTs and Smart contracts
Table of contents

- Overview
- Requirements
- Install
- Repository Structure
- Contrbutors


## Overview
This project will build and end to end web3 dApp that let's a client issue None Fungible Tokens as certificates that will represent the successful completion of a weekly challenge to trainees, and allow trainees with NFTs to interact with a smart contract to perform pre-defined actions. We will use the Algorand Blockchain as the foundational element of the NFT. This will solve the challenge of ensuring the authenticity of certificates offer to trainees.

## Requirements
> Python
>
> Pip
>
> py-algorand-skd 
>
> Flask
>
> Docker

## Install

1.Install the Algorand Sandbox environment locally
```
git clone https://github.com/algorand/sandbox.git
cd sandbox
./sandbox up
```
2.Install the project
```
git clone https://github.com/gedionabebe/Web3-Dapp.git
cd Web3-Dapp
pip install -r requirements.txt
```
## Repository Structure
```bash
├── .github/workflows(Github actions)
│   
├── algorand_dapp(The dapp's backend and frontend)
│
├── assests(Asset metadata)
│  
├── log(Log file)
│
├── notebooks(Jupyter notebooks)
│
├── screenshots(Algoexplorer and UI screenshots)
│
├── scripts(Python code)
│
├── tests(Unit tests)
│
├── README.md(Project information)
│
├── requirements.txt(Porject requirements)
```

## Contrbutors
- Gedion Abebe
