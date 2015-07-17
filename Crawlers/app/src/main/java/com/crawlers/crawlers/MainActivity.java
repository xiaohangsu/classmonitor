package com.crawlers.crawlers;

import android.app.ProgressDialog;
import android.content.Context;
import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.ActionBarActivity;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.Toast;


public class MainActivity extends ActionBarActivity {

    private Intent mIntent = new Intent();
    private Button ConfirmBtn;
    private Button Signup;
    private EditText email;
    private EditText password;
    private CheckBox mCheckBox;
    private Handler handler;
    private Runnable getMsg;
    private String Answer = "";
    private SharedPreferences sp;
    private Bundle mBundle = new Bundle();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        setTitle(R.string.Login_title);
        init();
    }

    private void init() {
        sp = this.getSharedPreferences("userinfo", Context.MODE_WORLD_READABLE);

        ConfirmBtn = (Button)findViewById(R.id.confirm);
        Signup = (Button)findViewById(R.id.signup);
        email = (EditText)findViewById(R.id.email);
        password = (EditText)findViewById(R.id.password);
        mCheckBox = (CheckBox)findViewById(R.id.checkBox);

        mCheckBox.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if (mCheckBox.isChecked()) {
                    sp.edit().putBoolean("isCheck", true).commit();
                } else {
                    sp.edit().putBoolean("isCheck", false).commit();
                }
            }
        });

        if (sp.getBoolean("isCheck", false)) {
            mCheckBox.setChecked(true);
            email.setText(sp.getString("email", ""));
            password.setText(sp.getString("password", ""));
        }

        /**
         * 登录按钮，启动登录线程并等待返回
         */
        ConfirmBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Answer = "";
                if (mCheckBox.isChecked()) {
                    sp.edit().putString("email", email.getText().toString()).commit();
                    sp.edit().putString("password", password.getText().toString()).commit();
                }

                final request MyRequest = new request(email.getText().toString(), password.getText().toString());
                MyRequest.startLoginThread();

                final ProgressDialog mProgressDialog = ProgressDialog.show(MainActivity.this, "wait", "waiting");

                handler = new Handler() {
                    public void handleMessage(Message msg) {
                        if (msg.what == 1) {
                            mProgressDialog.dismiss();
                            Toast.makeText(getApplicationContext(), "登录成功", Toast.LENGTH_SHORT).show();
                            mIntent.setClass(MainActivity.this, SubscribeActivity.class);
                            mBundle.putString("email", email.getText().toString());
                            mBundle.putString("password", password.getText().toString());
                            mIntent.putExtras(mBundle);
                            startActivity(mIntent);
                        } else if (msg.what == 2) {
                            mProgressDialog.dismiss();
                            Toast.makeText(getApplicationContext(), "登录失败", Toast.LENGTH_SHORT).show();
                        }
                    }
                };

                getMsg = new Runnable() {
                    @Override
                    public void run() {
                        String s1 = "true";
                        String s2 = "false";
                        if (Answer.equals(s1)) {
                            handler.obtainMessage(1).sendToTarget();
                        } else if (Answer.equals(s2)) {
                            handler.obtainMessage(2).sendToTarget();
                        } else {
                            Answer = MyRequest.getAnswer();
                            handler.postDelayed(getMsg, 100);
                        }
                    }
                };

                new Thread(getMsg).start();

            }
        });


        /**
         * 注册按钮，跳转到注册页面
         */
        Signup.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Intent mIntent = new Intent();
                mIntent.setClass(MainActivity.this, SignupActivity.class);
                startActivity(mIntent);
            }
        });

    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.menu_main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        int id = item.getItemId();

        //noinspection SimplifiableIfStatement
        if (id == R.id.action_settings) {
            return true;
        }

        return super.onOptionsItemSelected(item);
    }
}
