import Header from "../components/Header";

export default function Cadastro() {
    return (
        <>
            <div className="font-pressStart w-screen h-screen bg-charcoal flex flex-col items-center justify-center">
                <Header />
                <div className="bg-darkSlate w-1/2 h-3/4 flex flex-col justify-center items-center rounded gap-4 p-6">

                    {/* Nome */}
                    <input
                        name="name"
                        type="text"
                        placeholder="Nome"
                        className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                    />

                    {/* Email */}
                    <input
                        name="email"
                        type="email"
                        placeholder="Email"
                        className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                    />

                    {/* Senha */}
                    <input
                        name="password"
                        type="password"
                        placeholder="Senha"
                        className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                    />

                    {/* Função do usuário */}
                    <select
                        name="user_role"
                        className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                    >
                        <option value="">Selecione o papel</option>
                        <option value="0">Jogador</option>
                        <option value="1">Mestre</option>
                        <option value="2">Ambos</option>
                    </select>

                    {/* Imagem de perfil */}
                    <input
                        name="profile_image_path"
                        type="file"
                        accept="image/*"
                        className="p-2 rounded bg-charcoal text-offWhite w-2/3 text-base h-12"
                    />

                    {/* Botão de cadastro */}
                    <button
                        type="submit"
                        className="bg-deepRed hover:bg-forestGreen transition-colors text-offWhite rounded w-2/3 h-12 mt-4"
                    >
                        Cadastrar
                    </button>
                </div>
            </div>
        </>
    );
}
