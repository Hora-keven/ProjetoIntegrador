
let modalKey = 0


let quantcel = 1

let cart = []



const seleciona = (elemento) => document.querySelector(elemento)
const selecionaTodos = (elemento) => document.querySelectorAll(elemento)

const formatoReal = (valor) => {
    return valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', minimunFractionDigits: 2, maximumFractionDigits: 2, useGrouping: false })
}

const formatoMonetario = (valor) => {
    if(valor) {
        return valor.toFixed(2)
    }
}

const abrirModal = () => {
    seleciona('.celWindowArea').style.opacity = 0 
    seleciona('.celWindowArea').style.display = 'flex'
    setTimeout(() => seleciona('.celWindowArea').style.opacity = 1, 150)
}

const fecharModal = () => {
    seleciona('.celWindowArea').style.opacity = 0
    setTimeout(() => seleciona('.celWindowArea').style.display = 'none', 500)
}

const botoesFechar = () => {
   
    selecionaTodos('.celInfo--cancelButton, .celInfo--cancelMobileButton').forEach( (item) => item.addEventListener('click', fecharModal) )
}

const preencheDadosDasPizzas = (celItem, item, index) => {
   
	celItem.setAttribute('data-key', index)
    celItem.querySelector('.cel-item--img img').src = item.img
    celItem.querySelector('.cel-item--price').innerHTML = formatoReal(item.price[0])
    celItem.querySelector('.cel-item--name').innerHTML = item.name
    celItem.querySelector('.cel-item--desc').innerHTML = item.description
}

const preencheDadosModal = (item) => {
    seleciona('.celBig img').src = item.img
    seleciona('.celInfo h1').innerHTML = item.name
    seleciona('.celInfo--desc').innerHTML = item.description
    seleciona('.celInfo--actualPrice').innerHTML = formatoReal(item.price[0])
}


const pegarKey = (e) => {

    let key = e.target.closest('.cel-item').getAttribute('data-key')
    console.log('Celular clicado ' + key)
    console.log(celJson[key])


    quantcel = 1


    modalKey = key

    return key
}

const preencherTamanhos = (key) => {
   

    selecionaTodos('.celInfo--size').forEach((size, sizeIndex) => {

        (sizeIndex == 2) ? size.classList.add('selected') : ''
        size.querySelector('span').innerHTML = celJson[key]
    })
}



const mudarQuantidade = () => {
   
    seleciona('.celInfo--qtmais').addEventListener('click', () => {
        quantcel++
        seleciona('.celInfo--qt').innerHTML = quantcel
    })

    seleciona('.celInfo--qtmenos').addEventListener('click', () => {
        if(quantcel > 1) {
            quantcel--
            seleciona('.celInfo--qt').innerHTML = quantcel	
        }
    })
}



const adicionarNoCarrinho = () => {
    seleciona('.celInfo--addButton').addEventListener('click', () => {
        console.log('Adicionar no carrinho')

   
    	console.log("Celular " + modalKey)
    
	  
	
    	console.log("Quant. " + quantcel)
     
        let price = seleciona('.celInfo--actualPrice').innerHTML.replace('R$&nbsp;', '')
    
	    let identificador = celJson[modalKey].id+'t'

        let key = cart.findIndex( (item) => item.identificador == identificador )
        console.log(key)

        if(key > -1) {
         
            cart[key].qt += quantcel
        } else {
        
            let cel = {
                identificador,
                id: celJson[modalKey].id,
                qt: quantcel,
                price: parseFloat(price) 
            }
            cart.push(cel)
            console.log(cel)
            console.log('Sub total R$ ' + (cel.qt * cel.price).toFixed(2))
        }

        fecharModal()
        abrirCarrinho()
        atualizarCarrinho()
    })
}

const abrirCarrinho = () => {
    console.log('Qtd de itens no carrinho ' + cart.length)
    if(cart.length > 0) {
       
	    seleciona('aside').classList.add('show')
        seleciona('header').style.display = 'flex' 
    }

    seleciona('.menu-openner').addEventListener('click', () => {
        if(cart.length > 0) {
            seleciona('aside').classList.add('show')
            seleciona('aside').style.left = '0'
        }
    })
}

const fecharCarrinho = () => {

    seleciona('.menu-closer').addEventListener('click', () => {
        seleciona('aside').style.left = '100vw' 
        seleciona('header').style.display = 'flex'
    })
}

const atualizarCarrinho = () => {

	seleciona('.menu-openner span').innerHTML = cart.length
	
	
	if(cart.length > 0) {

	
		seleciona('aside').classList.add('show')


		seleciona('.cart').innerHTML = ''

   
		let subtotal = 0
		let desconto = 0
		let total    = 0

		for(let i in cart) {
		
			let celItem = celJson.find( (item) => item.id == cart[i].id )
			console.log(celItem)

        	subtotal += cart[i].price * cart[i].qt
          
			let cartItem = seleciona('.models .cart--item').cloneNode(true)
			seleciona('.cart').append(cartItem)


			let celName = `${celItem.name}`

			
			cartItem.querySelector('img').src = celItem.img
			cartItem.querySelector('.cart--item-nome').innerHTML = celName
			cartItem.querySelector('.cart--item--qt').innerHTML = cart[i].qt

		
			cartItem.querySelector('.cart--item-qtmais').addEventListener('click', () => {
				console.log('Clicou no botão mais')
				
				cart[i].qt++
		
				atualizarCarrinho()
			})

			cartItem.querySelector('.cart--item-qtmenos').addEventListener('click', () => {
				console.log('Clicou no botão menos')
				if(cart[i].qt > 1) {
				
					cart[i].qt--
				} else {
					
					cart.splice(i, 1)
				}

                (cart.length < 1) ? seleciona('header').style.display = 'flex' : ''

	
				atualizarCarrinho()
			})

			seleciona('.cart').append(cartItem)

		} 
		desconto = subtotal * 0
		total = subtotal - desconto

		
		seleciona('.subtotal span:last-child').innerHTML = formatoReal(subtotal)
		seleciona('.desconto span:last-child').innerHTML = formatoReal(desconto)
		seleciona('.total span:last-child').innerHTML    = formatoReal(total)

	} else {
	
		seleciona('aside').classList.remove('show')
		seleciona('aside').style.left = '100vw'
	}
}

const finalizarCompra = () => {
    seleciona('.cart--finalizar').addEventListener('click', () => {
        console.log('Finalizar compra')
        seleciona('aside').classList.remove('show')
        seleciona('aside').style.left = '100vw'
        seleciona('header').style.display = 'flex'
    })
}


celJson.map((item, index ) => {

    let celItem = document.querySelector('.models .cel-item').cloneNode(true)
  
    seleciona('.cel-area').append(celItem)

    preencheDadosDasPizzas(celItem, item, index)
    
    celItem.querySelector('.cel-item a').addEventListener('click', (e) => {
        e.preventDefault()
        console.log('Clicou no celular')

  
        let chave = pegarKey(e)
  

        abrirModal()

        preencheDadosModal(item)

 
        preencherTamanhos(chave)


		seleciona('.celInfo--qt').innerHTML = quantcel
       

    })

    botoesFechar()

}) 


mudarQuantidade()


adicionarNoCarrinho()
atualizarCarrinho()
fecharCarrinho()
finalizarCompra()

