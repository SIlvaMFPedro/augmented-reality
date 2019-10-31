import React, { Component } from "react";
import ReactDOM from "react-dom";
import PropTypes from "prop-types";

const PARAMETERS = [
  // Core config
  "detectionMode",
  "matrixCodeType",
  "cameraParametersUrl",
  "maxDetectionRate",
  // Source configuration
  "sourceType",
  "sourceUrl",
  "sourceWidth",
  "sourceHeight",
  // Canvas dimensions
  "displayHeight",
  "displayWidth",
  "canvasWidth",
  "canvasHeight",
  // Tracking module ['tango', 'artoolkit', 'best']
  "trackingMethod",
  "areaLearningButton",
  "performanceProfile",
  "tangoPointCloudEnabled",
  "debugUIEnabled"
];

/**
 * AFrameRenderer
 *
 * Render aframe.io primitives using a single marker
 *
 * Use multiple markers (independent) and render different objects
 *
 * Use camera as an entity or use cameraTransformMatrix (camera movement)
 *
 * Can also render aframe.io bindings for React (WebVR)
 *
 * Bugs/Errors to patch:
 *
 * AR.js gives this error 'THREEx.ArMarkerControls: 'markersAreaEnabled' is not a property of this material.'
 *
 * Why ?
 * - Composition
 * - DRY code
 * - Abstraction over artoolkit
 */

export default class AFrameRenderer extends Component {
  container = document.body;
  renderer = null;
  static propTypes = {
    arToolKit: PropTypes.shape({
      sourceType: PropTypes.string,
      sourceUrl: PropTypes.string,
      debugUIEnabled: PropTypes.bool,
      detectionMode: PropTypes.string,
      matrixCodeType: PropTypes.string,
      cameraParametersUrl: PropTypes.string,
      maxDetectionRate: PropTypes.number,
      sourceWidth: PropTypes.number,
      sourceHeight: PropTypes.number,
      displayWidth: PropTypes.number,
      displayHeight: PropTypes.number,
      canvasWidth: PropTypes.number,
      canvasHeight: PropTypes.number
    }),
    getSceneRef: PropTypes.func,
    inherent: PropTypes.bool
  };
  static defaultProps = {
    arToolKit: {},
    getSceneRef: () => {}, // No ref
    inherent: true // use modelViewMatrix
  };
  static childContextTypes = {
    inherent: PropTypes.bool
  };
}
