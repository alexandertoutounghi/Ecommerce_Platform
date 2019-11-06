// This will let us access important information from anywhere within the site
// export const nav = state => {
// 	return state.userInfo.nav;
// }
export const userInfo = state => {
	return state.userInfo;
}

export const goods_list = state => {
  console.log(state.goods_list)
  return state.goods_list;
}
