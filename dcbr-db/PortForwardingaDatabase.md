# Accessing a PostgreSQL Database Hosted in OpenShift

The following instructions assume:
1. You have the `oc` command line tool installed on your system and it is functioning.
1. You know how to login to an OpenShift server from the command line; using the login token from the web console.
1. You have permissions to access the project containing the database pod.
1. You have pgAdmin (or some other tool) installed and know how to use it.  The 

## Port forwarding to your local system

To accomplish this, we will use OpenShift port forwarding.  Some additional details on port forwarding can be found here; [Connecting to a Database Using Port Forwarding in OpenShift](https://blog.openshift.com/openshift-connecting-database-using-port-forwarding/).

- Login to the OpenShift server.
- Switch to the project containing the database pod.
  ```
  $ oc project nbup6o-dev
  Now using project "nbup6o-dev" on server "https://console.pathfinder.gov.bc.ca:8443".
  ```
- List the pods
  ```
  $ oc get pods
  NAME                            READY     STATUS    RESTARTS   AGE
  postgresql-8-xmjkx              1/1       Running   0          9d
  ```
- Port forward the PostgreSQL port to your local machine
  ```
  $ oc port-forward postgresql-oracle-fdw-1-hvrhz 5432:5432
  Forwarding from 127.0.0.1:5432 -> 5432
  Forwarding from [::1]:5432 -> 5432
  127.0.0.1:5432Handling connection for 5432
  Handling connection for 5432
  Handling connection for 5432
  ```

## Connecting pgAdmin

- Open pgAdmin
- Create a new Server and given it a name.
- On the connection tab enter;
  - Host Name: 127.0.0.1
  - Leave everything else as it's default.  Credentials are handled through the pod.
- Click save.

You should now be able to make queries.