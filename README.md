In the pursuit of making ec2 setup a little bit more failsafe and secure, I
wrote a little script to export the AWS credentials to environmental variables 

The functionality is as follows: 

  python export_env.py --access_id <AWS Access ID> --secret <AWS Secret Key> --export ~/<the file you want to write to>

Typically in a Unix environment, persistent environmental variables are stored
in ~/.bashrc

(These are things like $HOME (for home directory), $SHELL, etc.)

In the event that you are sourcing a different file for your env, I set this to
an argument. For example, you can feed it ~/.aws/credentials and it will write
the exports there. Once these are known in the environment, Java, Python, and
any other language will have a tool to read that variable from the env. 

If you want something to be known by the environment, you need to set it in a
profile. Which profile is read depends on the flavor of Unix and/or who is
calling the script. Amazon Linux appears to use /home/ec2-user/.bashrc, but if
you want the variables to be known to EVERY user, you would write instead to
/etc/profile (this would require sudo). 

Typical use of this tool, I’d expect, would write to ~/.bashrc as ec2-user.
From here, running env will return the variables we need, and the language
specific libraries will be able to access them. 

