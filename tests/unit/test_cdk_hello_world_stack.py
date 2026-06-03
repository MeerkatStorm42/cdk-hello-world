import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_hello_world.cdk_hello_world_stack import CdkHelloWorldStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_hello_world/cdk_hello_world_stack.py
def test_lambda_created():
    app = core.App()
    stack = CdkHelloWorldStack(app, "cdk-hello-world")
    template = assertions.Template.from_stack(stack)

    template.resource_count_is("Foo::Bar", 11)
