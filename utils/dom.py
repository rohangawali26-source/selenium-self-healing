def capture_dom(driver, tag):
    elements = driver.find_elements("xpath", f"//{tag}")
    dom = []

    for el in elements:
        dom.append({
            "element": el,
            "text": el.text.strip(),
            "tag": el.tag_name
        })

    return dom
