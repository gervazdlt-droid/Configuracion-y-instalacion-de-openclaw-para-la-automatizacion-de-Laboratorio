"""Ejemplo de acceso autorizado a una plataforma web.
Nunca guardes la contraseña en el código, en Git ni en capturas.
"""
import argparse, getpass, os
from pathlib import Path
from playwright.sync_api import sync_playwright


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--interactive", action="store_true")
    parser.add_argument("--headed", action="store_true", help="muestra el navegador")
    args = parser.parse_args()
    url = os.environ.get("LAB_PLATFORM_URL")
    user = os.environ.get("LAB_PLATFORM_USER")
    if not args.interactive or not url or not user:
        raise SystemExit("Usa --interactive y define LAB_PLATFORM_URL y LAB_PLATFORM_USER")
    password = getpass.getpass("Contraseña (no se guardará): ")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not args.headed)
        page = browser.new_page()
        page.goto(url, wait_until="domcontentloaded")
        # Adaptar selectores a la plataforma autorizada; no intenta evadir MFA/CAPTCHA.
        page.locator('input[name="username"], input[type="email"]').first.fill(user)
        page.locator('input[name="password"], input[type="password"]').first.fill(password)
        print("Formulario preparado. Revisa la ventana y confirma manualmente el envío.")
        if args.headed:
            input("Presiona Enter para cerrar sin enviar automáticamente... ")
        browser.close()

if __name__ == "__main__":
    main()
