package com.example.augmented_reality_android;

/**
 * IMPORTS
 */
import android.content.Context;
import android.hardware.Sensor;
import android.hardware.SensorEvent;
import android.hardware.SensorEventListener;
import android.hardware.SensorManager;


public class MyCurrentAzimuthal implements SensorEventListener{
    // Private Attributes
    private SensorManager sensorManager;
    private Sensor sensor;
    private int azimuthFrom = 0;
    private int azimuthTo = 0;
    private OnAzimuthalChangedListener mAzimuthalListener;
    Context mContext;

    /**
     * Constructor for MyCurrentAzimuthal Class
     */
    public MyCurrentAzimuthal(OnAzimuthalChangedListener azimuthalListener, Context context){
        mAzimuthalListener = azimuthalListener;
        mContext = context;
    }
    /**
     * MyCurrentAzimuthal Start Method
     */
    public void start(){
        sensorManager = (SensorManager) mContext.getSystemService(mContext.SENSOR_SERVICE);
        sensor = sensorManager.getDefaultSensor(Sensor.TYPE_ROTATION_VECTOR);
        sensorManager.registerListener(this, sensor, SensorManager.SENSOR_DELAY_UI);
    }
    /**
     * MyCurrentAzimuthal Stop Method
     */
    public void stop(){
        sensorManager.unregisterListener(this);
    }
    /**
     * MyCurrentAzimuthal Set Shake Listener Method
     * @param listener
     */
    public void setOnShakeListener(OnAzimuthalChangedListener listener) {
        mAzimuthalListener = listener;
    }

    /**
     * MyCurrentAzimuthal Sensor Changed Event Method
     * @param event
     */
    @Override
    public void onSensorChanged(SensorEvent event) {
        azimuthFrom = azimuthTo;
        float[] orientation = new float[3];
        float[] rMat = new float[9];
        SensorManager.getRotationMatrixFromVector(rMat, event.values);
        azimuthTo = (int) ( Math.toDegrees( SensorManager.getOrientation( rMat, orientation )[0] ) + 360 ) % 360;
        mAzimuthalListener.onAzimuthalChanged(azimuthFrom, azimuthTo);
    }

    /**
     * MyCurrentAzimuthal Sensor Accuracy Changed Method
     * @param sensor
     * @param accuracy
     */
    @Override
    public void onAccuracyChanged(Sensor sensor, int accuracy) {

    }

}
