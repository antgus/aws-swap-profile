# AWS Credentials Swap Default Profile Tool

A simple cli tool written in python for swapping the default AWS profile contained in `~/.aws/config`

Notes before executing the first time:
- Please backup your credentials file `~/.aws/credentials`
- Make sure that your existing `[default]` profile also exists under a different name (because the default profile will be overriden).


# Installation
1. Download [aws_default_profile_swap.py](aws_default_profile_swap.py) and move it to `~/.aws/aws_default_profile_swap.py`
2. Add the following content to your bash configuration file (`.zshrc`, or `~/.profile` or `~/.bashrc`):
```
# for swapping between different AWS profiles
aws-profile()
{
    echo swapping to $1
    python3 ~/.aws/aws_default_profile_swap.py $1
}
```


# Usage
`aws-swap PROFILE_NAME`

Example of a `credentials` file and `aws-swap` commands:
```config
[default]
aws_access_key_id = XXXX
aws_secret_access_key = YYYY
 
[personal-project]
aws_access_key_id = XXXX
aws_secret_access_key = YYYY
 
[work-project]
aws_access_key_id = ZZZZ
aws_secret_access_key = QQQQ
```

`aws-swap personal-project`

`aws-swap work-project`