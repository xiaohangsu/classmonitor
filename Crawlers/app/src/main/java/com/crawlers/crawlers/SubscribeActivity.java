package com.crawlers.crawlers;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

/**
 * Created by sury on 15-7-12.
 */
public class SubscribeActivity extends ActionBarActivity{

    private List<Map<String, String>> mDataList = new ArrayList<Map<String, String>>();
    private ListView mListView;
    private Handler handler;
    private Runnable getMsg;
    private SimpleAdapter mSimpleAdapter;
    private Button SubscribeBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_subscribe);
        setTitle(R.string.Subscribe_title);
        init();
    }

    private void init() {
        SubscribeBtn = (Button)findViewById(R.id.subButton);
        SubscribeBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        setData();
        Log.i("setData", mDataList.toString());

    }

    private void setData() {
        final request MyRequest = new request();
        MyRequest.startGetList();
        final ProgressDialog mProgressDialog = ProgressDialog.show(SubscribeActivity.this, "wait", "waiting");

        handler = new Handler() {
            public void handleMessage(Message msg) {
                if (msg.what == 1) {
                    mProgressDialog.dismiss();
                    mListView = (ListView)findViewById(R.id.classListView);
                    mSimpleAdapter = new SimpleAdapter(SubscribeActivity.this,
                            mDataList, R.layout.list_item,
                            new String[]{"source","class"},
                            new int[]{R.id.listSourceText, R.id.listClassText});
                    mListView.setAdapter(mSimpleAdapter);
                }
            }
        };

        getMsg = new Runnable() {
            @Override
            public void run() {
                if (!mDataList.isEmpty()){
                    Log.i("setDatabefore", mDataList.toString());
                    handler.obtainMessage(1).sendToTarget();
                } else {
                    mDataList = MyRequest.getMapList();
                    Log.i("setDatabemid", mDataList.toString());
                    handler.postDelayed(getMsg, 100);
                }
            }
        };
        new Thread(getMsg).start();
    }
}
