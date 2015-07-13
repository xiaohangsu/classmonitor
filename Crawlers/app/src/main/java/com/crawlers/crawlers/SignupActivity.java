package com.crawlers.crawlers;

import android.app.ProgressDialog;
import android.os.Bundle;
import android.os.Handler;
import android.os.Message;
import android.support.v7.app.ActionBarActivity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

/**
 * Created by sury on 15-6-21.
 */
public class SignupActivity extends ActionBarActivity {

    private Button signup_btn;
    private EditText email;
    private EditText name;
    private EditText psw1;
    private EditText psw2;
    private Handler handler;
    private Runnable getMsg;
    private String Answer = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_signup);
        setTitle(R.string.Signup_title);
        init();
    }

    public void init() {
        signup_btn = (Button)findViewById(R.id.signup_btn);
        email = (EditText)findViewById(R.id.signup_email);
        name = (EditText)findViewById(R.id.signup_name);
        psw1 = (EditText)findViewById(R.id.signup_psw1);
        psw2 = (EditText)findViewById(R.id.signup_psw2);

        signup_btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Answer = "";
                String email_s = email.getText().toString();
                String name_s = name.getText().toString();
                String psw1_s = psw1.getText().toString();
                String psw2_s = psw2.getText().toString();
                if (email_s.isEmpty()) {
                    Toast.makeText(getApplicationContext(), "邮箱不能为空", Toast.LENGTH_SHORT).show();
                } else if (name_s.isEmpty()) {
                    Toast.makeText(getApplicationContext(), "昵称不能为空", Toast.LENGTH_SHORT).show();
                } else if (psw1_s.isEmpty()) {
                    Toast.makeText(getApplicationContext(), "密码不能为空", Toast.LENGTH_SHORT).show();
                } else if (!psw1_s.equals(psw2_s)) {
                    Toast.makeText(getApplicationContext(), "两次输入密码不一致", Toast.LENGTH_SHORT).show();
                } else {
                    final request MyRequest = new request(email_s, name_s, psw1_s);
                    MyRequest.startSignupThread();

                    final ProgressDialog mProgressDialog = ProgressDialog.show(SignupActivity.this, "wait", "waiting");

                    handler = new Handler() {
                        public void handleMessage(Message msg) {
                            if (msg.what == 1) {
                                mProgressDialog.dismiss();
                                Toast.makeText(getApplicationContext(), "注册成功", Toast.LENGTH_SHORT).show();

                            } else if (msg.what == 2) {
                                mProgressDialog.dismiss();
                                Toast.makeText(getApplicationContext(), "注册失败:该用户已存在", Toast.LENGTH_SHORT).show();
                            }
                        }
                    };

                    getMsg = new Runnable() {
                        @Override
                        public void run() {
                            String s1 = "true";
                            String s2 = "false";
                            if (Answer.equals(s1)){
                                handler.obtainMessage(1).sendToTarget();
                            } else if (Answer.equals(s2)){
                                handler.obtainMessage(2).sendToTarget();
                            } else {
                                Answer = MyRequest.getAnswer();
                                handler.postDelayed(getMsg, 100);
                            }
                        }
                    };

                    new Thread(getMsg).start();
                }
            }
        });
    }
}
