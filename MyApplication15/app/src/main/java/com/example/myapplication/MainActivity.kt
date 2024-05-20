package com.example.myapplication
import android.app.Activity
import android.content.Intent
import android.os.Bundle
import android.speech.RecognizerIntent
import android.speech.SpeechRecognizer
import android.util.Log
import android.widget.ImageButton
import android.widget.TextView
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import okhttp3.Call
import okhttp3.Callback
import okhttp3.FormBody
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody
import okhttp3.Response
import okio.IOException
import java.util.Locale



class MainActivity : AppCompatActivity() {
    private  val RQ_SPEECH_REC = 1
    private lateinit var  btn_trans : ImageButton
    private lateinit var  txt : TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        btn_trans = findViewById(R.id.btn_tr)
        txt = findViewById(R.id.txt)
        btn_trans.setOnClickListener {
        txt.setText("")
        AskInput()

        } }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if(requestCode==RQ_SPEECH_REC && resultCode==Activity.RESULT_OK){
            val result :ArrayList<String>? = data?.getStringArrayListExtra(RecognizerIntent.EXTRA_RESULTS)
            val okhclient = OkHttpClient()
            val formBody: RequestBody = FormBody.Builder().add("text", result?.get(0).toString()).build()
            val request: Request = Request.Builder().post(formBody).url("http://172.16.74.51:5000//ConvertVoiceToText")
                .addHeader("Content-Type", "text/plain")
                .build()

            okhclient.newCall(request).enqueue(object : Callback {
                 override fun onResponse( call: Call, response: Response) {
                    val responseBodyString = response.body!!.string()
                     Log.d("succes" ,responseBodyString.toString())
                    runOnUiThread({txt.setText(responseBodyString) })  }
                 override fun onFailure( call: Call, e: IOException) {
                    Log.d("failedddddd" , result?.get(0).toString())
                    Log.d("failedddddd" ,e.toString())
                    runOnUiThread({txt.setText("failed")})
                 }
            })
            }}


    private fun AskInput() {
        if(!SpeechRecognizer.isRecognitionAvailable(this)){
            Toast.makeText(this , "speech recognition is not available " , Toast.LENGTH_SHORT).show()
        } else{
            val intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL ,RecognizerIntent.LANGUAGE_MODEL_FREE_FORM )
            intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE , Locale.getDefault())
            intent.putExtra(RecognizerIntent.EXTRA_PROMPT , "say something")
            startActivityForResult(intent,RQ_SPEECH_REC)}
    }
}
