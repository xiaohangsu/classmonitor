package com.crawlers.crawlers;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.ActionBarActivity;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.ListView;
import android.widget.SimpleAdapter;
import android.widget.TextView;
import android.widget.Toast;

import java.util.ArrayList;
import java.util.HashMap;
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
    private Button UserInfoBtn;
    private request MyRequest = new request();
    private Bundle mBundle;
    private Map<String, String> select_status = new HashMap<String, String>();


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_subscribe);
        setTitle(R.string.Subscribe_title);
        Bundle mBundle = this.getIntent().getExtras();
        init();
    }

    private void init() {
        mBundle = this.getIntent().getExtras();
        UserInfoBtn = (Button)findViewById(R.id.UserInfo);
        SubscribeBtn = (Button)findViewById(R.id.subButton);

        UserInfoBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Toast.makeText(getApplicationContext(), "当前用户是" +
                        mBundle.getString("email").toString(), Toast.LENGTH_SHORT).show();
            }
        });

        SubscribeBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                //MyRequest.startGetUserInfo();
                Log.i("count", mListView.getCheckedItemCount() + "");
                MyRequest = new request(mBundle.getString("email"), mBundle.getString("password").toString());
                Toast.makeText(getApplicationContext(), "操作成功", Toast.LENGTH_SHORT).show();
            }
        });

        setData();
        Log.i("setData", mDataList.toString());

    }


    /**
     * 先启动线程获取可订阅栏目，再设置listview的内容
     */
    private void setData() {
        MyRequest.startGetList();
        final ProgressDialog mProgressDialog = ProgressDialog.show(SubscribeActivity.this, "wait", "waiting");

        handler = new Handler() {
            public void handleMessage(Message msg) {
                if (msg.what == 1) {
                    mProgressDialog.dismiss();
                    mListView = (ListView)findViewById(R.id.classListView);
                    mListView.setChoiceMode(ListView.CHOICE_MODE_MULTIPLE);
                    mSimpleAdapter = new SimpleAdapter(SubscribeActivity.this,
                            mDataList, R.layout.list_item,
                            new String[]{"source","class","check"},
                            new int[]{R.id.listSourceText, R.id.listClassText, R.id.listCheckbox});

                    mListView.setAdapter(mSimpleAdapter);
                    mListView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
                        @Override
                        public void onItemClick(AdapterView<?> parent, View view, int position, long id) {
                            String source_s = ((TextView) view.findViewById(R.id.listSourceText)).getText().toString();
                            String class_s = ((TextView) view.findViewById(R.id.listClassText)).getText().toString();
                            if (select_status.containsKey(class_s)) {
                                select_status.remove(class_s);
                                //view.setBackgroundColor(Color.rgb(216, 216, 216));
                                ((CheckBox) view.findViewById(R.id.listCheckbox)).setChecked(false);
                            } else {
                                select_status.put(class_s, source_s);
                                //view.setBackgroundColor(Color.rgb(105, 105, 105));
                                ((CheckBox) view.findViewById(R.id.listCheckbox)).setChecked(true);
                            }
                            Log.i("shuzu", select_status.toString());
                        }
                    });
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
