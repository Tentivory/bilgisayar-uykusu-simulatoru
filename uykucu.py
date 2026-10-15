#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bilgisayar Uykusu Simulatoru
Bu kod GERCEKTEN calisir. Bilgisayariniz uyuyor gibi yapar.
"""

import time
import random
import sys

def bilgisayar_uykusu():
    print("Bilgisayar Uykusu Simulatoru v1.0 baslatiliyor...")
    print("Sistem hazirlaniyor... (uykuya geciyor)")
    time.sleep(2)
    
    while True:
        try:
            kullanici_girdisi = input("\nBir sey yazin (cikmak icin 'uyandir' yazin): ")
            if kullanici_girdisi.lower() == 'uyandir':
                print("Bilgisayar uyanmaya calisiyor... zzz... hayir hala uyuyor.")
                time.sleep(1)
                print("Tamam, uyandi. Hosca kal.")
                break
            
            # Uyku suresi: 3 ile 15 saniye arasi
            uyku_suresi = random.randint(3, 15)
            print(f"\nBilgisayar dusunuyor... (aslinda uyuyor, {uyku_suresi} saniye)")
            
            for i in range(uyku_suresi):
                print("z", end="", flush=True)
                time.sleep(1)
            print()
            
            cevaplar = [
                "zzzz... anladim ama yorgunum.",
                "Hmm... zzz... belki sonra.",
                "Sistem meşgul (uyuyor).",
                "Cevap: zzzzzzzzzz",
                "Bu girdi cok onemliydi. Ama uyku daha onemli."
            ]
            print(random.choice(cevaplar))
            
        except KeyboardInterrupt:
            print("\n\nBilgisayar zorla uyandirildi. Kizgin.")
            sys.exit(0)
        except Exception as e:
            print(f"Hata: Bilgisayar uyurken dusundu. {e}")

if __name__ == "__main__":
    bilgisayar_uykusu()

# Damga: Kayyum Grok - 2026-10-16
# Gizli: En iyisi secmen, en kotusu uyanmamak.