from machine import ADC, Pin

try:
    adc = ADC(Pin(0), atten=ADC.ATTN_11DB)
    print("✅ Attenuation supported! Using 11 dB (0–2.45V) range.")
    print("ADC read value:", adc.read())
except AttributeError as e:
    print("❌ Attenuation not supported on this firmware.")
    print("Error:", e)
except Exception as e:
    print("⚠️ Unexpected error:")
    print("Error:", e)
