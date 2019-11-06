package com.example.augmented_reality_android;

public class AugmentedPOI {
    // private attributes
    private int mId;
    private String mName;
    private String mDescription;
    private double mLatitude;
    private double mLongitude;

    /**
     * Constructor for AugmentedPOI class
     */
    public AugmentedPOI(String newName, String newDescription, double newLatitude, double newLongitude){
        this.mName = newName;
        this.mDescription = newDescription;
        this.mLatitude = newLatitude;
        this.mLongitude = newLongitude;
    }

    /**
     * Get Method for POI Id
     */
    public int getmId(){
        return mId;
    }
    /**
     * Set Method for POI Id
     */
    public void setmId(int poiId){
        this.mId = poiId;
    }
    /**
     * Get Method for POI Name
     */
    public String getmName(){
        return mName;
    }
    /**
     * Set Method for POI Name
     */
    public void setmName(String poiName){
        this.mName = poiName;
    }
    /**
     * Get Method for POI Description
     */
    public String getmDescription(){
        return mDescription;
    }
    /**
     * Set Method for POI Description
     */
    public void setmDescription(String poiDescription){
        this.mDescription = poiDescription;
    }
    /**
     * Get Method for POI Latitude
     */
    public double getmLatitude(){
        return mLatitude;
    }
    /**
     * Set Method for POI Latitude
     */
    public void setmLatitude(double poiLatitude){
        this.mLatitude = poiLatitude;
    }
    /**
     * Get Method for POI Longitude
     */
    public double getmLongitude(){
        return mLongitude;
    }
    /**
     * Set Method for POI Longitude
     */
    public void setmLongitude(double poiLongitude){
        this.mLongitude = poiLongitude;
    }
}
