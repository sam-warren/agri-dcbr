'use strict';
const {OpenShiftClientX} = require('pipeline-cli')
const path = require('path');

module.exports = (settings)=>{
  const phases = settings.phases
  const options = settings.options
  const oc=new OpenShiftClientX(Object.assign({'namespace':phases.build.namespace}, options));
  const phase='build'
  let objects = []
  const templatesLocalBaseUrl =oc.toFileUrl(path.resolve(__dirname, '../..'))

  objects.push(...oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/dcbr-web/openshift/templates/dcbr-web/dcbr-web-build.json`, {
    'param':{
      'NAME': `${phases[phase].name}${phases[phase].suffix}`,
      'GIT_REPO_URL': oc.git.http_url,
      'GIT_REF': oc.git.ref,
      'SOURCE_CONTEXT_DIR': '',
      'DOCKER_FILE_PATH': 'docker/dcbr-web/Dockerfile',
      'OUTPUT_IMAGE_TAG': phases[phase].tag
    }
  }));

  // The building of your cool app goes here ▼▼▼
  

  oc.applyRecommendedLabels(objects, phases[phase].name, phase, phases[phase].changeId, phases[phase].instance)
  oc.applyAndBuild(objects)
}