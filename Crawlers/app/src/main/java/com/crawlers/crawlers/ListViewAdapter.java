package com.crawlers.crawlers;

/**
 * Created by sury on 15-7-23.
 */
import java.util.List;
import java.util.Map;
import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.CheckBox;
import android.widget.SimpleAdapter;
import android.widget.TextView;

public class ListViewAdapter extends SimpleAdapter {
    private List<? extends Map<String, ?>> mArrayList;
    private int resource;
    private LayoutInflater mLayoutInflater;

    public ListViewAdapter(Context context,List<? extends Map<String, ?>> data, int resource, String[] from,int[] to) {
        super(context, data, resource, from, to);
        this.mArrayList = data;
        this.resource = resource;
        mLayoutInflater=(LayoutInflater) context.getSystemService(context.LAYOUT_INFLATER_SERVICE);
    }

    @Override
    public int getCount() {
        if (mArrayList==null) {
            return 0;
        } else {
            return mArrayList.size();
        }

    }

    @Override
    public Object getItem(int position) {
        if (mArrayList==null) {
            return null;
        } else {
            return mArrayList.get(position);
        }
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        ViewHolder viewHolder = null;
        if(convertView == null){
            viewHolder = new ViewHolder();
            convertView = mLayoutInflater.inflate(resource, null);
            viewHolder.sourceTextView = (TextView)convertView.findViewById(R.id.listSourceText);
            viewHolder.classTestView = (TextView)convertView.findViewById(R.id.listClassText);
            viewHolder.checkBox = (CheckBox)convertView.findViewById(R.id.listCheckbox);
            convertView.setTag(viewHolder);
        }else {
            viewHolder=(ViewHolder) convertView.getTag();
        }

        if (mArrayList!=null) {
            if (viewHolder.sourceTextView!=null) {
                viewHolder.sourceTextView.setText((String)(mArrayList.get(position).get("source")));
                viewHolder.classTestView.setText((String) (mArrayList.get(position).get("class")));
            }
            if (viewHolder.checkBox!=null) {
                boolean isChecked=SubscribeActivity.mCheckBoxStatusHashMap.get(position);
                viewHolder.checkBox.setChecked(isChecked);
            }
        }
        return convertView;
    }

    private class ViewHolder{
        TextView sourceTextView;
        TextView classTestView;
        CheckBox checkBox;
    }
}
