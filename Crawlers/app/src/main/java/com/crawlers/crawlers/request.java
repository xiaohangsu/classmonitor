package com.crawlers.crawlers;

import android.util.Log;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.DefaultHttpClient;
import org.json.JSONArray;
import org.json.JSONObject;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;


/**
 * Created by sury on 15-6-20.
 */
public class request {
    private static final String LoginNamespace = "http://128.199.91.212:5000/apiTemp/login";
    private static final String SignupNamespace = "http://128.199.91.212:5000/apiTemp/signup";
    private static final String getCatalogNameSpace = "http://128.199.91.212:5000/apiTemp/getNewsCatalog";
    private String email = "";
    private String password = "";
    private String name = "";
    private Map<String, String> mMap = new HashMap<String, String>();
    private ArrayList<Map<String, String>> mapList = new ArrayList<Map<String, String>>();
    private HashMap<String, String> result = new HashMap<String, String>();
    private ArrayList<Map<String, String>> tempList = new ArrayList<Map<String, String>>();

    public request(String email_, String password_) {
        email = email_;
        password = password_;
    }

    public request(String email_, String name_, String password_) {
        email = email_;
        name = name_;
        password = password_;
    }

    public request() {

    }

    public String getAnswer() {
        if (!result.containsKey("result")) {
            result.put("result", "");
        }
        return result.get("result").toString();
    }

    public ArrayList<Map<String, String>> getMapList() {
        return mapList;
    }

    public Thread LoginThread = new Thread(new Runnable() {
        @Override
        public void run () {
            try {
                JSONObject MyObj = new JSONObject();
                MyObj.put("loginID", email);
                MyObj.put("email", email);
                MyObj.put("password", password);

                HttpPost httpPost = new HttpPost(LoginNamespace);
                httpPost.addHeader("Content-Type", "application/json");
                httpPost.setEntity(new StringEntity(MyObj.toString()));

                HttpClient httpClient = new DefaultHttpClient();
                HttpResponse response = httpClient.execute(httpPost);

                result = getFromJson(response);

            } catch (Exception e) {
                e.printStackTrace();
            }
        }

    });

    public HashMap<String, String> getFromJson(HttpResponse r) {
        try {
            StringBuilder builder = new StringBuilder();

            BufferedReader bufferedReader = new BufferedReader(
                    new InputStreamReader(r.getEntity().getContent()));

            for (String s = bufferedReader.readLine(); s != null; s = bufferedReader.readLine()) {
                builder.append(s);
                Log.i("s:", s);
            }

            JSONObject jsonObject = new JSONObject(builder.toString());
            String k = jsonObject.getString("result");
            HashMap<String, String> temp = new HashMap<String, String>();
            temp.put("result", jsonObject.get("result").toString());
            return temp;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return result;
    }

    public ArrayList<Map<String, String>> getList(HttpResponse r) {
        try {
            StringBuilder builder = new StringBuilder();

            BufferedReader bufferedReader = new BufferedReader(
                    new InputStreamReader(r.getEntity().getContent()));

            for (String s = bufferedReader.readLine(); s != null; s = bufferedReader.readLine()) {
                builder.append(s);
                Log.i("s:", s);
            }

            HashMap<String, String> temp = new HashMap<String, String>();

            JSONObject jsonObject_1 = new JSONObject(builder.toString());
            JSONArray jsonArray = new JSONArray(jsonObject_1.get("data").toString());

            tempList = new ArrayList<Map<String, String>>();

            for (int i = 0; i < jsonArray.length(); i++) {
                JSONObject jsonObject = new JSONObject(jsonArray.get(i).toString());

                String s2 = jsonObject.getString("list").toString();
                String[] tempString = null;

                tempString = s2.split(",");

                ArrayList<String> mString = new ArrayList<>();

                for (int l = 0; l < tempString.length; l++) {
                    mString.add(tempString[l].split("\"")[1]);
                    mMap = new HashMap<String, String>();
                    mMap.put("source", jsonObject.getString("source").toString());
                    mMap.put("class", mString.get(l).toString());
                    Log.i("mMap", mMap.toString());
                    tempList.add(mMap);
                }
            }
            return tempList;
        } catch (Exception e) {
            e.printStackTrace();
        }
        return tempList;
    }

    public void startLoginThread() {
        LoginThread.start();
    }

    public Thread SignupThread = new Thread(new Runnable() {
        @Override
        public void run() {
                try {
                    JSONObject MyObj = new JSONObject();
                    MyObj.put("loginID", email);
                    MyObj.put("email", email);
                    MyObj.put("name", name);
                    MyObj.put("password", password);

                    HttpPost httpPost = new HttpPost(SignupNamespace);
                    httpPost.addHeader("Content-Type", "application/json");
                    httpPost.setEntity(new StringEntity(MyObj.toString()));

                    HttpClient httpClient = new DefaultHttpClient();
                    HttpResponse response = httpClient.execute(httpPost);

                    result = getFromJson(response);

                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
    });

    public void startSignupThread() {
        SignupThread.start();
    }

    public Thread SubscribeThread = new Thread(new Runnable() {
        @Override
        public void run() {
            try {

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    });

    public void startSubscribeThread() {
        SubscribeThread.start();
    }

    public Thread getList = new Thread(new Runnable() {
        @Override
        public void run() {
            try {
                HttpPost httpPost = new HttpPost(getCatalogNameSpace);
                HttpClient httpClient = new DefaultHttpClient();
                HttpResponse response = httpClient.execute(httpPost);
                mapList = getList(response);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    });

    public  void startGetList() {
        getList.start();
    }

}


