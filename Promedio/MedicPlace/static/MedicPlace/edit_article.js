document.addEventListener("DOMContentLoaded",function(){
    get_article=document.querySelector("#edit_article");
    article_id=get_article.getAttribute("data-article_id");
    article_title=document.querySelector("#title_article");
    article_content=document.querySelector("#content_article");
    texarea_title=document.querySelector("#texarea_title");
    texarea_content=document.querySelector("#textarea_content");
    get_article.addEventListener("click",function(){
        if (get_article.textContent=="Edit Article") {
            get_article.textContent="Save"
            article_title.style.display="none"
            article_content.style.display="none"
            texarea_title.style.display="block"
            texarea_content.style.display="block"
        } else if (get_article.textContent=="Save") {
            get_article.textContent="Edit Article"
           
            texarea_title.style.display="none"
            texarea_content.style.display="none"
            // Chaging content of page
            article_title.textContent=texarea_title.value
            article_content.textContent=texarea_content.value
            edit_Article(article_id,texarea_title.value,texarea_content.value)
            article_title.style.display="block"
            article_content.style.display="block"
        }
        
    })
    function edit_Article(id,title,content){
        form= new FormData;
        form.append("title",title);
        form.append("content",content);
        fetch(`${id}`,{
            method:"POST",
            body:form,
        })
        .then((res) => res.json())
        .then((res) => {
            article_title.textContent=res.title2
            article_content.textContent=res.content2
        })  
    }
    

})