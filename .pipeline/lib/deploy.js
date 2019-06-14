'use strict';
const {OpenShiftClientX} = require('pipeline-cli')
const path = require('path');

module.exports = (settings)=>{
  const phases = settings.phases
  const options= settings.options
  const phase=options.env
  const changeId = phases[phase].changeId
  const oc=new OpenShiftClientX(Object.assign({'namespace':phases[phase].namespace}, options));
  const templatesLocalBaseUrl =oc.toFileUrl(path.resolve(__dirname, '../..'))
  var objects = []

  // The deployment of your cool app goes here ▼▼▼
  objects.push(...oc.processDeploymentTemplate(`${templatesLocalBaseUrl}/dcbr-web/openshift/templates/dcbr-web/dcbr-web-deploy.json`, {
    'param':{
      'NAME': `${phases[phase].name}${phases[phase].suffix}`,
      'APP_GROUP': `${phases[phase].name}${phases[phase].suffix}`,
      'IMAGE_NAMESPACE': `${phases.build.namespace}`,
      'IMAGE_NAME': `${phases.build.name}${phases.build.suffix}`,
      'TAG_NAME': `${phases.build.tag}`,
      'APPLICATION_DOMAIN': phases[phase].domain
    }
  }));

  oc.applyRecommendedLabels(objects, phases[phase].name, phase, `${changeId}`, phases[phase].instance)
  oc.importImageStreams(objects, phases[phase].tag, phases.build.namespace, phases.build.tag)
  oc.applyAndDeploy(objects, phases[phase].instance)
}
