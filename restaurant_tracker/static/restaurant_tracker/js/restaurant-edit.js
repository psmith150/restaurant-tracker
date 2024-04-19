let addButton = document.querySelector("#add-menu-item")
addButton.addEventListener('click', addMenuItem)
$(function () {
    $('#restaurant-form').areYouSure(
        {
            message: 'It looks like you have been editing something. '
                + 'If you leave before saving, your changes will be lost.'
        }
    );
});

function addMenuItem(e) {
    e.preventDefault()
    const url = JSON.parse(document.getElementById('create-url').textContent)
    fetch(url).then(
        (response) => {
            if (response.status != 200) {
                console.log("Error retrieving new menu item from server.")
                return Promise.reject("Error getting new menu item from server.")
            }
            return response.json()
        })
        .then(dataJson => {

            let menuForms = document.querySelectorAll(".menu-item-row")
            let menuNum = menuForms.length - 1
            let menuContainer = document.querySelector("#restaurant-form")
            let totalMenuItems = document.querySelector("#id_menuitem_set-TOTAL_FORMS")

            let newData = dataJson[0]
            let newMenuItem = menuForms[0].cloneNode(true)
            let menuItemIdRegex = RegExp(`menu-item-row-(\\d)+`, 'g')
            let menuItemFormRegex = RegExp(`menuitem_set-(\\d)+`, 'g')
            menuNum++
            newMenuItem.id = newMenuItem.id.replace(menuItemIdRegex, `menu-item-row-${menuNum}`)
            newMenuItem.innerHTML = newMenuItem.innerHTML.replace(menuItemFormRegex, `menuitem_set-${menuNum}`)
            // Set to data from response
            newMenuItem.querySelector(`#id_menuitem_set-${menuNum}-name`).setAttribute("value", `${newData["fields"]["name"]}`)
            //newMenuItem.innerHTML.querySelector(`#id_menuitem_set-${menuNum}-user`).setAttribute("value", `${newData["fields"]["user"]}`)
            newMenuItem.querySelector(`#id_menuitem_set-${menuNum}-date`).setAttribute("value", `${newData["fields"]["date"]}`)
            newMenuItem.querySelector(`#id_menuitem_set-${menuNum}-price`).setAttribute("value", `${newData["fields"]["price"]}`)
            //newMenuItem.innerHTML.querySelector(`#id_menuitem_set-${menuNum}-rating`).setAttribute("value", `${newData["fields"]["rating"]}`)
            newMenuItem.querySelector(`#id_menuitem_set-${menuNum}-comment`).setAttribute("value", `${newData["fields"]["comment"]}`)
            menuForms[menuNum - 1].after(newMenuItem)
            totalMenuItems.setAttribute('value', `${menuNum + 1}`)
        })
}