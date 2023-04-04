from invoke import task

@task
def start(ctx):
    ctx.run("python3 src/all/main.py", pty=True)

@task
def test(ctx):
    ctx.run("pytest src/tests/tests.py", pty=True)

@task
def coverage(ctx):
    ctx.run("coverage run --branch -m pytest src/tests/tests.py", pty=True)

@task(coverage)
def coverage_report(ctx):
    ctx.run("coverage html", pty=True)