package com.example.augmented_reality_android;

/**
 * IMPORTS
 */
import android.content.Context;
import android.location.Location;
import android.os.Bundle;
import android.util.Log;
import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.location.LocationListener;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;



public class MyCurrentLocation
        implements GoogleApiClient.ConnectionCallbacks, GoogleApiClient.OnConnectionFailedListener, LocationListener {
    // Private Attributes
    private GoogleApiClient mGoogleApiClient;
    private Location mLastLocation;
    private LocationRequest mLocationRequest;
    private OnLocationChangedListener onLocationChangedListener;

    /**
     * Constructor for MyCurrentLocation class
     */
    public MyCurrentLocation(OnLocationChangedListener onLocationChangedListener) {
        this.onLocationChangedListener = onLocationChangedListener;
    }

    /**
     * Build Google Client API Method
     */
    protected synchronized void buildGoogleApiClient(Context context) {
        mGoogleApiClient = new GoogleApiClient.Builder(context)
                .addConnectionCallbacks(this)
                .addOnConnectionFailedListener(this)
                .addApi(LocationServices.API)
                .build();
        mLocationRequest = LocationRequest.create()
                .setPriority(LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY)
                .setInterval(10 * 1000)     // 10 seconds in milliseconds
                .setFastestInterval(1000); // 1 second in milliseconds
    }

    /**
     * MyCurrentLocation Start Method
     */
    public void start() {
        mGoogleApiClient.connect();
    }

    /**
     * MyCurrentLocation Stop Method
     */
    public void stop() {
        mGoogleApiClient.disconnect();
    }

    /**
     * MyCurrentLocation OnConnected Method
     */
    @Override
    public void onConnected(Bundle bundle) {
        LocationServices.FusedLocationApi.requestLocationUpdates(mGoogleApiClient, mLocationRequest, this);
        mLastLocation = LocationServices.FusedLocationApi.getLastLocation(mGoogleApiClient);
        if (mLastLocation != null) {
            onLocationChangedListener.onLocationChanged(mLastLocation);
        }
    }

    /**
     * MyCurrentLocation OnConnectionSuspended Method
     */
    @Override
    public void onConnectionSuspended(int i) {
    }

    /**
     * MyCurrentLocation OnConnectionFailed Method
     */
    @Override
    public void onConnectionFailed(ConnectionResult connectionResult) {
        Log.e("MyApp",
            "Location services connection failed with code " + connectionResult.getErrorCode());
    }

    /**
     * MyCurrentLocation OnLocationChanged Method
     */
    @Override
    public void onLocationChanged(Location location) {
        mLastLocation = LocationServices.FusedLocationApi.getLastLocation(
                mGoogleApiClient);
        if (mLastLocation != null) {
            onLocationChangedListener.onLocationChanged(mLastLocation);
        }
    }
}

