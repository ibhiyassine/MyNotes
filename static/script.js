document.addEventListener("DOMContentLoaded", function()
{
    let full = document.querySelectorAll(".full");
    let unfull = document.querySelectorAll(".unfull");
    for (let i = 0; i< full.length; i++)
    {
        let f = full[i];
        let uf = unfull[i];
        let container = f.parentElement;
        full[i].addEventListener("click", function(){
            container.className="after_container";
            f.style.visibility = "hidden";
            f.style.width = "0px";
            f.style.padding = "unset";
            uf.style.visibility = "visible";
            uf.style.width = "initial";
            uf.style.padding = "initial";
        });
        unfull[i].addEventListener("click", function(){
            container.className="container";
            uf.style.visibility = "hidden";
            uf.style.width = "0px";
            uf.style.padding = "unset";
            f.style.visibility = "visible";
            f.style.width = "initial";
            f.style.padding = "initial";
        });
    }
});