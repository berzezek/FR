export const setCookie = (name: string, value: string, days: number) => {
    var expires = "";
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days*24*60*60*1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires;
}

export const getCookie = (name: string): string | undefined => {
  const value = "; " + document.cookie;
  const parts = value.split("; " + name + "=");
  if (parts.length == 2) { // @ts-ignore
      return parts.pop().split(";").shift();
  }
  return undefined;
}

export const eraseCookie = (name: string) => {
    document.cookie = name+'=; Max-Age=-99999999;';
}
