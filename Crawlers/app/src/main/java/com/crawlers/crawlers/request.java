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
import java.util.Iterator;
import java.util.Map;


/**
 * Created by sury on 15-6-20.
 */
public class request {
    private static final String LoginNamespace = "http://128.199.91.212:5000/apiTemp/login";
    private static final String SignupNamespace = "http://128.199.91.212:5000/apiTemp/signup";
    private static final String getCatalogNameSpace = "http://128.199.91.212:5000/apiTemp/getNewsCatalog";
    private static final String getUserInfoSpace = "http://128.199.91.212:5000/apiTemp/get";
    private static final String updateUserSpace = "http://128.199.91.212:5000/apiTemp/update";
    private static final String EmailSpace = "http://128.199.91.212:5000/apiTemp/sendEmail";

    private String email = "";
    private String password = "";
    private String name = "";
    private Map<String, String> subscribe = new HashMap<String, String>();
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

    public request(String email_, Map<String, String> subscribe_) {
        email = email_;
        subscribe = subscribe_;
    }

    public request() {

    }

    /***
     ** getAnswer: 获取注册成功与否的标志
     ***/

    public String getAnswer() {
        if (!result.containsKey("result")) {
            result.put("result", "");
        }
        return result.get("result").toString();
    }

    /***
        getMapList: 获取可订阅的栏目列表
     ****/
    public ArrayList<Map<String, String>> getMapList() {
        return mapList;
    }


    /**
     * 登录线程
     */
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

                DefaultHttpClient httpClient = new DefaultHttpClient();
                HttpResponse response = httpClient.execute(httpPost);
                result = getFromJson(response);

            } catch (Exception e) {
                e.printStackTrace();
            }
        }

    });
    public void startLoginThread() {
        LoginThread.start();
    }

    /**
     *
     * @param r HTTP POST请求返回的HttpResponse
     * @return 解析JSON后的信息，含有请求是否成功的标志
     */
    public HashMap<String, String> getFromJson(HttpResponse r) {
        try {
            StringBuilder builder = new StringBuilder();

            BufferedReader bufferedReader = new BufferedReader(
                    new InputStreamReader(r.getEntity().getContent()));

            for (String s = bufferedReader.readLine(); s != null; s = bufferedReader.readLine()) {
                builder.append(s);
                Log.i("getUserInfo:", s);
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


    /**
     *
     * @param r HTTP POST请求返回的HttpResponse
     * @return 解析JSON后的Map数组，含有所有可订阅栏目的信息
     */
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
                    mMap.put("check", ""+ l);
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

    /**
     * 登录线程，请求后返回登录成功与否的标志
     */

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


    /**
     * 未实现的订阅线程
     */
    public Thread SubscribeThread = new Thread(new Runnable() {
        @Override
        public void run() {
            try {
                if (subscribe.size() > 0) {
                    JSONObject sendData = new JSONObject();
                    JSONArray subData = new JSONArray();
                    Iterator iter_ = subscribe.entrySet().iterator();
                    while (iter_.hasNext()) {
                        Map.Entry entry = (Map.Entry) iter_.next();
                        String key = (String)entry.getKey();
                        subData.put(key);
                    }
                    sendData.put("subscribe", subData);
                    sendData.put("loginID", email);

                    Log.i("datasend", sendData.toString());

                    HttpPost httpPost = new HttpPost(updateUserSpace);
                    HttpPost httpSendEmail = new HttpPost(EmailSpace);

                    httpPost.addHeader("Content-Type", "application/json");
                    httpSendEmail.addHeader("Content-Type", "application/json");
                    httpPost.setEntity(new StringEntity(sendData.toString(), "utf-8"));
                    httpSendEmail.setEntity(new StringEntity(sendData.toString(), "utf-8"));

                    HttpClient httpClient = new DefaultHttpClient();
                    HttpClient httpEmailClient = new DefaultHttpClient();
                    HttpResponse response = httpClient.execute(httpPost);
                    HttpResponse responseE = httpEmailClient.execute(httpSendEmail);
                    //result = getFromJson(response);
                    Log.i("!!!!!!1", result.toString());
                }
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

    public Thread getUserInfo = new Thread(new Runnable() {
        @Override
        public void run() {
            try {
                HttpPost httpPost = new HttpPost(getUserInfoSpace);
                HttpClient httpClient = new DefaultHttpClient();
                HttpResponse response = httpClient.execute(httpPost);
                result = getFromJson(response);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    });
    public void startGetUserInfo() {
        getUserInfo.start();
    }

    public Thread updateUser = new Thread(new Runnable() {
        @Override
        public void run() {
            try {
                JSONObject MyObj = new JSONObject();
                MyObj.put("loginID", email);
                MyObj.put("password", password);

                HttpPost httpPost = new HttpPost(updateUserSpace);
                HttpClient httpClient = new DefaultHttpClient();
                httpPost.addHeader("Content-Type", "application/json");
                httpPost.setEntity(new StringEntity(MyObj.toString()));

                HttpResponse response = httpClient.execute(httpPost);
                result = getFromJson(response);
            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    });
}


