ARG base_image
FROM ${base_image}

ENV STI_SCRIPTS_PATH=/usr/libexec/s2i

LABEL io.k8s.display-name="dcbr-api s2i" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,python,dcbr-api" \
      io.openshift.s2i.scripts-url="image:///${STI_SCRIPTS_PATH}"

# Add dcbr user - we will use this to run the image
RUN useradd -ms /bin/bash dcbr

# Copy the S2I scripts from the specific language image to $STI_SCRIPTS_PATH.
COPY --chown=dcbr:0 ./s2i/bin/. $STI_SCRIPTS_PATH

# Copy the utility scripts to /usr/local/bin
COPY --chown=dcbr:0 ./bin/. /usr/local/bin

USER root

# - In order to drop the root user, we have to make some directories world
#   writable as OpenShift default security model is to run the container
#   under random UID.
RUN usermod -a -G 0 dcbr && \
    chmod -R ug+rwx $STI_SCRIPTS_PATH

USER dcbr

WORKDIR /opt/app-root/src

EXPOSE 8080

# Set the default CMD to print the usage of the language image.
CMD $STI_SCRIPTS_PATH/usage