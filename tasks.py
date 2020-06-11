# Task definitions for invoke
# You must first install invoke, https://www.pyinvoke.org/

# You can also create you own tasks
from invoke import task

from metapack_build.tasks.package import ns, dummy

# To configure options for invoke functions you can:
# - Set values in the 'invoke' section of `~/.metapack.yaml
# - Use one of the other invoke config options:
#   http://docs.pyinvoke.org/en/stable/concepts/configuration.html#the-configuration-hierarchy
# - Set the configuration in this file:

# ns.configure(
#    {
#        'metapack':
#            {
#                's3_bucket': 'bucket_name',
#                'wp_site': 'wp sot name',
#                'groups': None,
#                'tags': None
#            }
#    }
# )

# However, the `groups` and `tags` hould really be set in the `metatada.csv`
# file, and `s3_bucket` and `wp_site` should be set at the collection or global level

# Override publication. 
ns.add_task(dummy, 'publish')

# Remove publication
@task(optional=['force'])
def make(c, force=None, s3_bucket=None, wp_site=None, groups=[], tags=[]):
    """Build, write to S3, and publish to wordpress, but only if necessary"""

    groups = c.metapack.groups or groups
    tags = c.metapack.tags or tags

    wp_site = c.metapack.wp_site or wp_site
    s3_bucket = c.metapack.s3_bucket or s3_bucket

    force_flag = '-F' if force else ''

    group_flags = ' '.join([f"-g{g}" for g in groups])
    tag_flags = ' '.join([f"-t{t}" for t in tags])


    c.run(f'mp --exceptions -q  make {force_flag}  -r  -b ', pty=True)



@task
def example_task(c):
    """An exmaple Invoke task"""
    c.run("echo 'this is an example task' ")


ns.add_task(example_task)
