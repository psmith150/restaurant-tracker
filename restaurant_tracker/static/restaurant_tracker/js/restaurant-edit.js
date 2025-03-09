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
            return response.text()
        })
        .then(dataText => {
            let menuForms = document.querySelectorAll(".menu-item-row")
            let menuNum = Math.max(menuForms.length, 0)
            let totalMenuItems = document.querySelector("#id_menuitem_set-TOTAL_FORMS")
            let menuItemIdRegex = RegExp(`menu-item-row-(\\d)+`, 'g')
            let menuItemFormRegex = RegExp(`menuitem_set-(\\d)+`, 'g')
            let menuItemPrefixRegex = RegExp(`__prefix__`, 'g')
            dataText = dataText.replace(menuItemIdRegex, `menu-item-row-${menuNum}`)
            //dataText = dataText.replace(menuItemFormRegex, `menuitem_set-${menuNum}`)
            dataText = dataText.replace(menuItemPrefixRegex, `${menuNum}`)
            
            document.getElementById('menu-items-table').insertAdjacentHTML('beforeend', dataText)
            menuNum++
            totalMenuItems.setAttribute('value', `${menuNum}`)
        })
}