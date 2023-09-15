<p align="center"><img src="./readme_images/dog_and_robot.png" width=500 /></p>

**Periodical ArXiv Digest to your personal Email 📚.** 

Trying to keep up with all those new papers on Arxiv?
Find yourself forgetting to check on it once a while?
Want to automate the entire process and get Digested data directly to your Email?

This repo while help you do exactly that ✅

## 🔍 What this repo does

Staying up to date on [arXiv](https://arxiv.org) papers can take a considerable amount of time, with on the order of hundreds of new papers each day to filter through. 

This repository offers a method to curate a daily digest.

* You modify the configuration file `config.yaml` with an arXiv Subject, and some set of Categories.
* The code sends an email with the digested HTML report using SMTP, periodically (as you desire)!

### Running as a github action using SMTP (Recommended).

The recommended way to get started using this repository is to:

1. Fork the repository
2. Modify `config.yaml` and merge the changes into your main branch.
3. Set the following secrets [(under settings, Secrets and variables, repository secrets)](https://docs.github.com/en/actions/security-guides/encrypted-secrets#creating-encrypted-secrets-for-a-repository).
   - `EMAIL_ADDRESS` - Your email address for which the digest while be sent to.
   - `EMAIL_APP_PASSWORD` - Generate a App password - (https://support.google.com/accounts/answer/185833?hl=en).
   - `GH_TOKEN` Token for the workflow being able to commit to its own repo (for digest persistence over time)
4. Manually trigger the action or wait until the scheduled action takes place.

> **WARNING:** Do not edit and commit your `.env.template` with your personal keys or email address! Doing so may expose these to the world!

## Roadmap
- [x] Support Arxiv digest
- [x] Support SMTP integration
- [ ] Support Github repos digest




## 💁 Extending and Contributing

The repo is forked from https://github.com/AutoLLM/ArxivDigest/tree/main, a great repo that also uses LLMs for paper relevance sorting. 
For my purposes, i needed a simple repo without relaying on OpenAI (and others that have rate limit issues).

