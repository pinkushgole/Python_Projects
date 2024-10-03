
from deep_translator import GoogleTranslator


def change(text="type"):
   try:
       translator = GoogleTranslator(source='auto', target='en')
       translation = translator.translate(text)
       return translation
   except Exception as e:
        print(f"Error during translation: {e}")
        response_text = "Translation failed. Please try again later."

print(change("""साधारण रूप से निबंध के विषय परिचित विषय होते हैं, यानी जिनके बारे में हम सुनते, देखते व पढ़ते रहते हैं; जैसे – धार्मिक त्योहार, राष्ट्रीय त्योहार, विभिन्न प्रकार की समस्याएँ, मौसम आदि।
जीवन के सभी क्षेत्रों में सफल विचार-विमर्श के लिए हमें श्रेष्ठ निबंध लेखन की आवश्वयकता होती है। निबंध‍ किसी भी विषय पर लिखा जा सकता है। आज सामाजिक, आर्थिक, राजनीतिक और वैज्ञानिक विषयों पर निबंध लिखे जा रहे हैं। संसार का हर विषय, हर वस्तु, व्यक्ति एक निबंध का केंद्र हो सकता है।
हिंदी के प्रमुख साहित्यकार आचार्य रामचंद्र शुक्ल ने निबन्ध को परिभाषित करते हुए कहा है-
“निबन्ध लेखन में लेखक अपने मन की प्रवृत्ति के अनुसार स्वच्छंद गति से इधर-उधर फूटी हुई सूत्र शाखाओं पर विचरता चलता है।"""))