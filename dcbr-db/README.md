# Database(s)

## Development

The DB component is an instance of Postgres, and the image being used is an unchanged Red Hat image. As such, there is no build or database initialization associated with the DB - just the Deployment.

## Deployment

To deploy the AGRI-DCBR database on an instance of OpenShift, use the [OpenShift Developer Tools](https://github.com/BCDevOps/openshift-developer-tools).

## Connecting a database tool to a database instance

Refer to [Accessing a PostgreSQL Database Hosted in OpenShift](./PortForwardingaDatabase.md) for details on how to connect to an instance of a database hosted in OpenShift using port forwarding.
