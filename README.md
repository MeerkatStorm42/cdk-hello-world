
# Modified AWS CDK Hello World Example.

Originally, this example was from [HERE](https://docs.aws.amazon.com/cdk/v2/guide/serverless-example.html) .

Then, I decided to add GitHub Actions to it.
And, instead of ```cdk synth``` , I used the cycle of ```cdk diff``` and then ```cdk deploy``` .
As from one workplace, I learnt that the ```diff``` step provides a more readable, truncated view than the JSON with ```synth``` (just imho, too).