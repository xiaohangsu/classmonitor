package com.crawlers.crawlers;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.ActionBarActivity;
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

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_subscribe);
        setTitle(R.string.Subscribe_title);
        init();
    }

    private void init() {
        setData();
        mListView = (ListView)findViewById(R.id.classListView);

        final SimpleAdapter mSimpleAdapter = new SimpleAdapter(this,
                mDataList, R.layout.list_item,
                new String[]{"source","class"},
                new int[]{R.id.listSourceText, R.id.listClassText});

        mListView.setAdapter(mSimpleAdapter);
    }

    private void setData() {
        final request MyRequest = new request();
        MyRequest.startGetList();
        final ProgressDialog mProgressDialog = ProgressDialog.show(SubscribeActivity.this, "wait", "waiting");

        handler = new Handler() {
            public void handleMessage(Message msg) {
                if (msg.what == 1) {
                    mProgressDialog.dismiss();
                }
            }
        };

        getMsg = new Runnable() {
            @Override
            public void run() {
                if (!mDataList.isEmpty()){
                    handler.obtainMessage(1).sendToTarget();
                } else {
                   mDataList = MyRequest.getMapList();
                    handler.postDelayed(getMsg, 100);
                }
            }
        };
        new Thread(getMsg).start();
    }
}
