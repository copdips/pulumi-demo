"""A Python Pulumi program"""

import pulumi
import pulumi_databricks as databricks

clu = databricks.get_cluster(cluster_name="Unity-catalog")
clu_pol = databricks.get_cluster_policy(name="Job Compute")
cu = databricks.get_current_user()
cuo = databricks.get_current_user_output()
pulumi.export('clu', clu)
pulumi.export('clu_pol', clu_pol)
pulumi.export('cu', cu)
pulumi.export('cuo', cuo)
